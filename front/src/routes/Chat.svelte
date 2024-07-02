<script>
    /**
     * @typedef Message
     * @type {object}
     * @property {string} author - the author.
     * @property {string} message - the message
     */
    /** @type {Message[]} */
    let messages = [];

    let newMessage = "";

    async function sendMessage() {
        if (newMessage.trim()) {
            messages = [...messages, { author: "Client", message: newMessage }];

            const response = await fetch("http://localhost:8000/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    message: newMessage,
                    history: messages,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                messages = [
                    ...messages,
                    { author: "Agent", message: data.message },
                ];
            } else {
                console.error("Failed to fetch response from server");
            }
        }
    }
</script>

<div class="chat-container">
    <div class="messages">
        {#each messages as { author, message }}
            <div class="message {author}">
                <strong>{author}:</strong>
                {message}
            </div>
        {/each}
    </div>
    <div class="input-container">
        <input
            type="text"
            bind:value={newMessage}
            placeholder="Type your message..."
            on:keypress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button on:click={sendMessage}>Send</button>
    </div>
</div>

<style>
    .chat-container {
        display: flex;
        flex-direction: column;
        height: 90vh;
        max-width: 600px;
        margin: 0 auto;
        border: 1px solid #ccc;
        border-radius: 8px;
        overflow: hidden;
    }
    .messages {
        flex: 1;
        padding: 10px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
    }
    .input-container {
        display: flex;
        border-top: 1px solid #ccc;
        padding: 10px;
    }
    input {
        flex: 1;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        margin-right: 10px;
    }
    button {
        padding: 10px 20px;
        border: none;
        background-color: #007bff;
        color: white;
        border-radius: 4px;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
    .message {
        margin: 5px 0;
        padding: 10px;
        border-radius: 5px;
        max-width: 80%;
    }
    .Client {
        background-color: #daf5cb;
        align-self: flex-start;
    }
    .Agent {
        background-color: #f0f0f0;
        align-self: flex-end;
    }
</style>
