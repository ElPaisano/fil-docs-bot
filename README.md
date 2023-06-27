# FilDocsBot

> FilDocsBot is a hacky experiment, not a production-ready application :D

FilDocsBot is a chatbot application that answers users questions about Filecoin using the [official documentation](https://docs.filecoin.io/). 
The bot uses the [Superpowered AI Python SDK](https://github.com/SuperpoweredAI/superpowered-python-sdk) to provide ChatGPT with a "knowledge base" (the official Filecoin docs),
so that ChatGPT will not make up wacky answers using unknown or outdated sources. In other words, Superpowered AI provides guardrails, so that ChatGPT only draws from sources provided and does not hallucinate. 

The bot then uses this knowledge to answer questions about Filecoin that the user asks via the command line. The bot also cites the document used to answer the question.

## How to use the bot

As described above, FilDocsBot is currently an experiemental app. As such, setting it up and using it is a little hacky.

### Prerequisites

1. Python 3.10.9 or higher

1. The Superpowered AI Python SDK

    ```shell
    pip install superpowered-sdk
    ```
    
1. The OpenAI Python SDK

    ```shell
    pip install openai
    ```
    
1. An OpenAI account 

1. An OpenAI API key

1. A Superpowered AI key and key secret

1. A text editor 

1. A terminal application

### Setup

Once you've met the prerequisites, you must complete some intital set up to use the bot.

1. Clone this repository:

   ```shell
   git clone https://github.com/ElPaisano/fil-docs-bot.git
   ```
   
1. Navigate to the `fil-docs-bot` repository:

   ```shell
   cd fil-docs-bot
   ```
   
1. In your favorite text editor, open `create_kb.py`.

1. Enter your Superpowered API key and secret on the correct lines, which should now look something like:

   ```shell
   os.environ["SUPERPOWERED_API_KEY_ID"] = "fake-key-12ey31811kjhgjk03"
   os.environ["SUPERPOWERED_API_KEY_SECRET"] = "fake-secret-86483264289342893"
   ```
   
1. Close and save the file.

1. In a terminal, run `create_kb.py` to create the knowledge base that the bot will use to answer questions.

   ```shell
   python create_kb.py
   ```
   
   The script outputs a knowledge base ID in the terminal. **You will need this in next steps, so don't forget it.**
   
   ```shell
   Created knowledge base with id: da8abde5-6b55-4e51-b396-863fd7bfb35b
   ```

1. In your favorite text editor, open `chat.py`.

1. On the correct lines, enter the following info:

   - Your Superpowered AI key and secret
   - Your OpenAI API key
   - The ID of the knowledge base you created

   Your `chat.py` should look something like:
   
   ```shell
   os.environ["OPENAI_API_KEY"] = "fake-z6HVRmnFAKENXzdptT3BlbkFJhp4"
   os.environ["SUPERPOWERED_API_KEY_ID"] = "fake1123256789"
   os.environ["SUPERPOWERED_API_KEY_SECRET"] = "alsofake-cewyb56789YYhbjdg"

   knowledge_base_id = "532fake259-109f-478a-aa63-fe3c0ab3d3ab"
   ```

1. Close and save the file.

Yay! You've completed the setup! Now, you can use the bot.

### Use the bot

Now that the set up is complete, fire up the bot and start asking questions. 

> A note on latency: Responses to questions may experience a latency of at least a few seconds and the terminal may hang briefly.

1. Run the bot.

   ```shell
   python chat.py
   ```
   
   You should see something like:
   
   ```shell
   GREETINGS HUMAN, I WILL ANSWER YOUR QUESTIONS ABOUT FILECOIN. BOOP.
   ...
   ENTER YOUR QUESTION BELOW.


   USER: 
   ```
1. In the `USER` field, type your question and press the **ENTER** key. Here's an example question and response:

   ```shell
   USER: What is Filecoin?

   CHATBOT: Filecoin is a decentralized storage network that allows users to store files on a peer-to-peer network with built-in economic incentives and cryptography to ensure files are stored reliably over time. 
   Users pay to store their files on storage providers, who are responsible for storing files and proving they have stored them correctly over time. 
   Filecoin facilitates open markets for storing and retrieving files that anyone can participate in. 
   It is built on top of the same software powering IPFS protocol and has an incentive layer on top to incentivize contents to be reliably stored and accessed. 
   You can learn more at https://docs.filecoin.io/basics/what-is-filecoin/overview/.
   ```

> To exit the application, type `exit` in the `USER` field and press the **ENTER** key.
