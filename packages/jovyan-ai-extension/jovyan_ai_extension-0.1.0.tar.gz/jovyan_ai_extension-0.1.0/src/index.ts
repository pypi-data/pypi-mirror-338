import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { INotebookTracker } from '@jupyterlab/notebook';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { JovyanCellController } from './cellOps/jovyanCellController';
import { NotebookController } from './controller';
import { initializeClient } from './jovyanClient';

/**
 * Initialization data for the jovyan-ai-extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jovyan-ai-extension:plugin',
  description: 'A JupyterLab extension to integrate Jovyan AI',
  autoStart: true,
  requires: [INotebookTracker],
  optional: [ISettingRegistry],
  activate: async (
    app: JupyterFrontEnd,
    notebookTracker: INotebookTracker,
    settingRegistry: ISettingRegistry | null
  ) => {
    console.debug(
      'JupyterLab extension jovyan-ai-extension is activated! Hello!'
    );

    // Initialize settings if settingRegistry is available
    if (settingRegistry) {
      await initializeClient(settingRegistry);

      // Listen for setting changes
      settingRegistry
        .load('jovyan-ai-extension:plugin')
        .then(settings => {
          settings.changed.connect(async () => {
            await initializeClient(settingRegistry);
          });
        })
        .catch(error => {
          console.error(
            'Failed to load settings for jovyan-ai-extension:',
            error
          );
        });
    }

    const notebookController = new NotebookController(
      notebookTracker,
      app.commands
    );

    // on notebook active cell changed, add the cell activate button
    notebookTracker.activeCellChanged.connect((sender, cell) => {
      if (cell) {
        const jovyanCellController = new JovyanCellController(
          cell,
          notebookController
        );
        jovyanCellController.activate();
      }
    });
  }
};

export default plugin;
