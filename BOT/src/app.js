require('dotenv').config();
const express = requires('express');
const app = express();
const PORT = process.env.PORT || 3001;

app.get('/', (req,res) => {
    res.send('Hello');
});

app.get('/dashboard', (req,res) =>{
    res.json({
        msg: 'Good',
        status:200
    })
});

app.listen(PORT, ()=>{
    console.log(`Now listening to requests on port ${PORT}`);
});

const express = require("express");
const app = express();

app.listen(3000, () => {
    console, log("Project is running!");
})

app.get("/", (req, res) => {
    res.send("Hello world!");
})

const Discord = require("discord.js");
const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES"] });

client.on("message", message => {
    if (message.content === "ping") {
        message.channel.send("pong");
    }

})

client.login(process.env.token);
