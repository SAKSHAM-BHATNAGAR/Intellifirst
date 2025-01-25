// Async function to fetch a message
async function fetchAsyncMessage() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("This is an async message!");
        }, 1000); // Simulate a 1-second delay
    });
}

// Main function to print messages
async function printMessages() {
    console.log("First message"); // Immediate print
    const asyncMessage = await fetchAsyncMessage(); // Wait for async message
    console.log(asyncMessage); // Print after 1 second
    console.log("Third message"); // Print immediately after the async message
}

// Call the main function
printMessages();