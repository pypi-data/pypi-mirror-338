import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ILauncher } from '@jupyterlab/launcher';

import { requestAPI } from './handler';

import { ServerConnection } from '@jupyterlab/services';

/**
 * The command IDs used by the server extension plugin.
 */

/**
 * Initialization data for the @jupyterlab-examples/server-extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@sinaraml/sinaraml_jupyter_host_ext:plugin',
  description:
    'A minimal JupyterLab extension with backend and frontend parts.',
  autoStart: true,
  optional: [ILauncher],
  requires: [],
  activate: (
    app: JupyterFrontEnd,
    launcher: ILauncher | null
  ) => {
    console.log(
      'JupyterLab extension @sinaraml/sinaraml_jupyter_host_ext is activated!'
    );

    // Try avoiding awaiting in the activate function because
    // it will delay the application start up time.
    const settings = ServerConnection.makeSettings()
    const _url = settings.baseUrl
    const dataToSend = { server_url: _url };
    requestAPI<any>('set_server_url', {
      body: JSON.stringify(dataToSend),
      method: 'POST'
    })
      .then(reply => {
        console.log(reply);
      })
      .catch(reason => {
        console.error(
          `Error on POST /sinaraml-jupyter-host-ext/set_server_url ${dataToSend}.\n${reason}`
        );
      });
  }
};

export default plugin;
