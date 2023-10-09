const fs = require('fs');
const { exec } = require('child_process');
const { v4: uuidv4 } = require('uuid'); // Import the UUID v4 function

// Generate a UUID
const uuid = uuidv4();

// Create a dynamic file name with the UUID
const folderName = 'report';

// Create the folder if it doesn't exist
if (!fs.existsSync(folderName)) {
    fs.mkdirSync(folderName);
}

// Create a dynamic file name with the UUID inside the "report" folder
const fileName = `${folderName}/${uuid}.txt`;

// Text content you want to write to the file
const fileContent = 'Hello, this is the content of the dynamically named file!';

// Use the writeFile method to create the file and write content to it
fs.writeFile(fileName, fileContent, (err) => {
    if (err) {
        console.error('Error creating the file:', err);
    } else {
        console.log(`File "${fileName}" has been created successfully.`);
    }
});

const branch = process.env.branch;

console.log(`current branch ${branch}`);

// Set git user name locally
const command1 = `git config --local user.name ${process.env.username}`;
exec(command1, (error1, stdout1, stderr1) => {
    if (error1) {
        console.error(`Error setting git user name: ${error1}`);
        return;
    }

    console.log(`Git user name set locally: ${process.env.username}`);

    // Configure global git settings
    exec('git config --global --add --bool push.autoSetupRemote true', (error2, stdout2, stderr2) => {
        if (error2) {
            console.error(`Error configuring git: ${error2}`);
            return;
        }

        // Checkout the branch
        exec(`git checkout -b ${branch}`, (error3, stdout3, stderr3) => {
            if (error3) {
                console.error(`Error checking out branch: ${error3}`);
                return;
            }

            console.log(`Checked out branch: ${branch}`);

            const htmlFilePath = 'report'; // Replace with the actual HTML file path
            // Add, commit, pull, and push
            exec(`git add ${htmlFilePath}`, (error4, stdout4, stderr4) => {
                if (error4) {
                    console.error(`Error adding file: ${error4}`);
                    return;
                }

                console.log(`Added file: ${htmlFilePath}`);

                exec('git commit -m "Updated coverage file"', (error5, stdout5, stderr5) => {
                    if (error5) {
                        console.error(`Error committing changes: ${error5}`);
                        return;
                    }

                    console.log('Committed changes.');

                    exec(`git pull origin ${branch}`, (error6, stdout6, stderr6) => {
                        if (error6) {
                            console.error(`Error pulling changes: ${error6}`);
                            return;
                        }

                        console.log(`Pulled changes from origin ${branch}.`);

                        exec('git push', (error7, stdout7, stderr7) => {
                            if (error7) {
                                console.error(`Error pushing changes: ${error7}`);
                                return;
                            }

                            console.log('Pushed changes to the remote repository.');
                        });
                    });
                });
            });
        });
    });
});


