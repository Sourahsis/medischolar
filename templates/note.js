const{ PythonShell } = require("python-shell");



let options = { scriptPath: "C:\Users\soura\Desktop\blueprint\website\home",};
 PythonShell.run("profile.py", options, (err, res) => {
if (err) console.log(err);
if (res) console.log(res);
 });
