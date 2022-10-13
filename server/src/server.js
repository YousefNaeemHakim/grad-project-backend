const express = require('express');
const dotenv = require('dotenv');
const colors = require('colors');
const connectDB = require('./config/db');

// Load env variables
dotenv.config({ path: './config/config.env'});

// Connect to database
connectDB();

// Router Files

const app = express();

app.use(express.json());

const PORT = process.env.PORT || 5000;

const server = app.listen(
    PORT,
    console.log(`Server running in ${process.env.NODE_ENV} mode on port ${PORT}`.yellow.italic)
);

// Handle unhandled promise rejections
process.on('unhandledRejection', (err , promise) => {
    console.log(`Error: ${err.message}`.red);
    // Close server & exit process
    server.close(() => process.exit(1));
});