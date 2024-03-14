# Examples
This folder contains instruction of how to run this app:
* [Running Locally](#running-locally)
  * [1. Clone the Git Repo](#1-clone-the-git-repo)
  * [2. Setup Local Environment](#2-local-environment-setup)
* [Deployment](#deployment)
* [Web Application](#web-application)

<a id="running-locally"></a>
## Running the App Locally

<a id="1-clone-the-git-repo"></a>
### 1. Clone the Git Repo
Run the following `git` command:
```bash
git clone https://github.com/DSProjects2024/thronetalk-game-of-thrones-summarizer
```

<a id="2-local-environment"></a>
### 2. Local Environment Setup
To create the 'thronetalks' conda environment which contains all the required packages to run the app, run these commands:

```bash
conda env create -f environment.yml
conda activate thronetalks
```
The second commande activates the specific environemnt.


If you want to deactivate this environment in the future, then use the command:
```bash
conda deactivate
```

If you want to delete this environment, then use the following command:
```bash
conda remove --name thronetalks --all
```


<a id="4-run-the-app"></a>
### 4. Run the App
The app can be run on the localhost using the following command.
```bash
streamlit run an_analysis_of_nothing/app.py
```
Make sure to activae conda before doing this using
```bash
conda activate thronetalks
```
if not done already.



Enjoy the experience of using Game of Thrones Summarizer right on your browser!!

<a id="deployment"></a>
## Deployment


The app is hosted as a Streamlit app here: **[throne-talk.streamlit.app](https://throne-talk.streamlit.app/)**

<a id="web-application"></a>
## Web Application
* Click [here](./site_navigation.md) for a website walk-through with text.
* There is also a visual [Video Demonstration](https://drive.google.com/file/d/1GadkwGMEtFOznwmvRZYv9gkUYwnhFoLj/view?usp=sharing).