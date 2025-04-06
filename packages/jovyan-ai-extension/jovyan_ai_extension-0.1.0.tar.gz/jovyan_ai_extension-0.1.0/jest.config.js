const jestJupyterLab = require('@jupyterlab/testutils/lib/jest-config');

const baseConfig = jestJupyterLab(__dirname);

module.exports = {
  ...baseConfig,
  automock: false,
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/.ipynb_checkpoints/*'
  ],
  coverageReporters: ['lcov', 'text'],
  testRegex: 'src/.*/.*.spec.ts[x]?$',
  transformIgnorePatterns: [
    '/node_modules/(?!(@jovyan|@jupyter|@jupyterlab|@microsoft|@codemirror|exenv-es6|lib0|nanoid|vscode-ws-jsonrpc|y-protocols|y-websocket|yjs)/)'
  ]
};
