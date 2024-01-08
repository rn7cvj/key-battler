// import { app, ipcMain, BrowserWindow } from 'electron';
// import { exec } from 'child_process';
// import * as electron from "electron";
//
// const startURL = 'http://localhost:5000';
//
// function createWindow() {
//     // Create the browser window.
//     const { width, height } = electron.screen.getPrimaryDisplay().workAreaSize;
//     const win = new electron.BrowserWindow({
//         width,
//         height,
//         webPreferences: {
//             nodeIntegration: true,
//             contextIsolation: false,
//             enableRemoteModule: true,
//         },
//     });
//
//     win.loadURL(startURL);
//
//     // Open the DevTools.
//     win.webContents.openDevTools();
// }
//
// app.whenReady().then(() => {
//     createWindow();
//
//     app.on('activate', function () {
//         if (BrowserWindow.getAllWindows().length === 0) createWindow();
//     });
// });
//
// app.on('window-all-closed', function () {
//     if (process.platform !== 'darwin') app.quit();
// });
//
// ipcMain.handle('execute-command', async (event, command) => {
//     return new Promise((resolve, reject) => {
//         exec(command, (error, stdout, stderr) => {
//             if (error) {
//                 reject(new Error(error.message));
//                 return;
//             }
//             if (stderr) {
//                 reject(new Error(stderr));
//                 return;
//             }
//             resolve(stdout.trim());
//         });
//     });
// });