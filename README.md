<h1 align="center">Turkish-Chatbot</h1> 

A chatbot is a computer program or an artificial intelligence (AI) that is designed to simulate human conversation through text or speech interactions. It is also commonly referred to as a conversational agent or virtual assistant.

Chatbots are programmed to understand and respond to user queries and provide relevant information or assistance. They can be integrated into various platforms such as websites, messaging apps, or voice assistants, allowing users to engage in conversations and receive automated responses.

There are different types of chatbots, ranging from rule-based chatbots to more advanced AI-powered chatbots. Rule-based chatbots follow a predefined set of rules and responses, while AI-powered chatbots use natural language processing (NLP) and machine learning techniques to understand and generate more contextually appropriate responses.

Chatbots can be used for a variety of purposes, such as customer support, information retrieval, task automation, and entertainment. They can improve efficiency by handling repetitive or common queries, provide 24/7 availability, and enhance user experiences by delivering personalized interactions.


<details>
<summary><h3 align="left">Data Preparation</h2></summary>
Necessary data is collected from the path education in Miuul websites and faq section of bootcamps in VBO websites. Question and answers are collected by using web scraping via BeautifulSoup library. But scraping data from websites is not enough for training a chatbot. So, we need more question and answers to train our chatbot. For this purpose, we added some questions and answers manually,then we saved it as a xlsx file.

This dataset covered subjects such as: bootcamp name, program location, program price, program duration, program start date, program end date, program description, program curriculum, program requirements ext.

The data is converted from xlsx file to json file so that chatbot returns the answer of the question that user asked.
</details>


<details>
<summary><h3 align="left">Data Preprocessing</h2></summary>
Firstly, we deleted html tags from the data. Then, we converted all the letters to lowercase. After that, we removed punctuation marks and stopwords, which are words that do not add meaning to the sentence, from our dataset.

Finally, we tokenized the data by using lemmatization. We used n-gram that creates combinations of words used together. Here, we created consecutive strings consisting of n elements according to the n number we determined.
</details>


<details>
<summary><h3 align="left">Visualization</h2></summary>
For visualization, we used word cloud. Word cloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance. Significant textual data points can be highlighted using a word cloud.

<img width="960" alt="bot1" src="img/vbo_wc.jpg">

<img width="960" alt="bot1" src="img/miuul_wc.jpg">

</details>


<details>
<summary><h3 align="left">Modeling</h2></summary>
We created neural network model by using Keras. We used ReLU activation function for the input layer and the hidden layers, and a softmax activation function for the output layer. We used categorical_crossentropy as the loss function, and the adam optimizer. We trained the model for 500 epochs. We saved the model as a h5 file.
</details>


<details>
<summary><h3 align="left">Web Integration</h2></summary>
We used HTML and CSS to design the interface of the chatbot website. We integrated the chatbot into the website with FLASK.
</details>


<details>
<summary><h3 align="left">Output</h2></summary>

<img width="960" alt="bot1" src="https://user-images.githubusercontent.com/53316818/216295182-f7b7f66d-00b1-4b24-b6a2-27c147318104.png">

<img width="960" alt="bot2" src="https://user-images.githubusercontent.com/53316818/216295272-47fbe9a4-931b-4842-8d30-7b1b4837f12b.png">

<img width="960" alt="bot3" src="https://user-images.githubusercontent.com/53316818/216295264-8aca87e7-4409-4930-a2ec-d063f1ac459e.png">

<img width="960" alt="bot4" src="https://user-images.githubusercontent.com/53316818/216295282-2fc9a843-0966-47ea-96b9-0dc08743ac85.png">

<img width="960" alt="bot5" src="https://user-images.githubusercontent.com/53316818/216295308-bc9809ad-70f3-4504-ad58-b861545d2fdd.png">

</details>


