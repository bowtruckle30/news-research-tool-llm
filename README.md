# news-research-tool-llm
<h3>App overview</h3>
<img width="1468" alt="Screenshot 2024-02-21 at 3 04 17 PM" src="https://github.com/bowtruckle30/news-research-tool-llm/assets/25841184/b92459b1-d6b8-4a9b-ad52-e121f048d666">
<br>
<br>

<img width="1470" alt="Screenshot 2024-02-21 at 3 10 31 PM" src="https://github.com/bowtruckle30/news-research-tool-llm/assets/25841184/38c1e21b-67a8-407b-83d0-19f37d128b7e">



<h3>Features</h3>
<ul>
<li>Load URLs or upload text files containing URLs to fetch article content.</li>
<li>Process article content through LangChain's UnstructuredURL Loader.</li>
<li>Construct an embedding vector using OpenAI's embeddings and leverage FAISS, a powerful similarity search library, to enable swift and effective retrieval of relevant information.</li>
<li>Interact with the LLM's (Chatgpt) by inputting queries and receiving answers along with source URLs.</li>
</ul>

<h3>Usage/Examples</h3>
1. Run the Streamlit app by executing: <br>
streamlit run main.py

<br>
2.The web app will open in your browser.

<ul>
<li>On the sidebar, you can input URLs directly.</li>

<li>Initiate the data loading and processing by clicking "Process URLs."</li>

<li>Observe the system as it performs URL loading, text splitting, generates embedding vectors, and efficiently indexes them using FAISS.</li>

<li>The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.</li>

<li>One can now ask a question and get the answer based on those news articles.</li>
</ul>

<h3>Project Structure </h3>
<ul>
<li>notebooks: reference guide directory for text loaders, splitters, FAISS index, open ai embeddings, genreating vectors, and retrieval.</li>
<li>main.py: The main Streamlit application script.</li>
<li>requirements.txt: A list of required Python packages for the project.</li>
<li>.env: Configuration file for storing your OpenAI API key.</li>
</ul>
