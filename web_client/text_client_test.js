// taken from archipelago.js documentation

import readline from "node:readline";

import { Client } from "archipelago.js";

// Using the node readline module, create an interface for intercepting any user input.
const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: false });

const client = new Client();

client.messages.on("message", (content) => {
    console.log(content);
});

// Add an event listener for when a "line" is entered into the standard input (e.g., the console/terminal window).
rl.on("line", async (line) => {
    // Send the input!
    await client.messages.say(line)
});

client.login("archipelago.gg:51496", "StuffdewValley")
    .then(() => console.log("Connected to the Archipelago server!"))
    .catch(console.error);