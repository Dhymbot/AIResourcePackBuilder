// To be fair im probably changing to Python for this project this might be a lot easier considering the awful performance on terminal for interactive programs

const { version } = require('./package.json');
const { loadEnvFile } = require('node:process');
const path = require('path');
const fs = require('fs');

loadEnvFile();
const { ORIGINAL_ROUTE, OUTPUT_ROUTE, API_PORT, FORCE_FORMAT, TEXTURE_RESOLUTION } = process.env;

let packFormat = 0;
let blockStr = "blocks";
let itemStr = "items";
if (FORCE_FORMAT) packFormat = FORCE_FORMAT;
else {
    const { pack } = JSON.parse(fs.readFileSync(path.join(ORIGINAL_ROUTE, 'pack.mcmeta')));
    packFormat = pack.pack_format;
}
if (packFormat >= 4) {
    blockStr = "block";
    itemStr = "item";
}

const originalBlocks = fs.readdirSync(path.join(ORIGINAL_ROUTE, '/assets/minecraft/textures/', blockStr));
const originalItems = fs.readdirSync(path.join(ORIGINAL_ROUTE, '/assets/minecraft/textures/', itemStr));


console.log(`
/----------------------------------------------------\\    
|                    WELCOME TO                      |
|                    THE BUILDER                     |    
\\----------------------------------------------------/
    `);
console.log(`- App version: ${version}\n- Pack format: ${packFormat}\n- Original: ${ORIGINAL_ROUTE}\n- Output: ${OUTPUT_ROUTE}\n- Texture Resolution: ${TEXTURE_RESOLUTION}x`);


console.log('The program has cached every file name of the blocks and items textures successfully.');
console.log('Now, the program needs to generate the prompt for each image to generate. You can add details to each prompt and you\'ll need to check each one.');

// Creating prompts listed
function blockFolder() {
    console.log('| Block Folder');
    const promptsBlocks = [];
    for (const block of originalBlocks) {
        console.log(block);
    }
}