# Github-Automated-Analysis | Langchain-OpenAI Submission Project

## Github Automated Analysis | To Find Out Most Technically Complex And Challenging Repo

A Python-based tool which, when given a GitHub user's URL, returns the most technically complex and challenging repository from that user's profile. The tool will use GPT and LangChain to assess each repository individually before determining the most technically challenging one. 
1. Fetch a user’s repositories from their GitHub user URL. 
2. Preprocess the code in repositories before passing it into GPT. 
4. Identify which of the repositories is the most technically complex. 
5. Deployed on streamlit cloud. The interface has a simple text box where users can input a GitHub user URL for analysis. Then, it process and display a link to the most complex repository as well as GPT analysis justifying the selection.

Check Here [Deployed Link](https://vksmadheshiya-github-automated-analysis-main-ywgobj.streamlit.app/)

Watch Here [Youtube](https://www.youtube.com/watch?v=vx7O8UcOfwM)


## Steps To Run
1. Create a venv (optional)
2. Install Requirements `pip install -r requirements.txt` 
3. Update openai_key in constants.py file ([openai api-keys](https://platform.openai.com/account/api-keys))
4. Run The main File by `streamlit run main.py`


After Running This Code A UI Will Appear asking for `GitHub User's URL For Analysis`:
Please Enter GitHub User's URL in TextField and wait for some time (it will take some time to calculate)








