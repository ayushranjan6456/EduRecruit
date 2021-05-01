# Project Name: Edurecreuit
# Problem Statement ✨

An online system to validate student information for the hiring process.

Every time there is a new hire, companies need to run a verification process with third parties to cross-check the information provided by candidates. You need to design an application where companies can verify student’s certificates/ degrees from various universities/ institutes/ course providers. The application needs to have some features where companies can list the job profile for which they are hiring. This algorithm will help analyze the job or skills demand in the market.

# What it does 🤖
We are aiming to create a web application to make the hiring process for companies easier. The application will store information about aspiring candidates who can either be students or currently working professionals. And the application will have information about the companies that are providing job opportunities. We create a model that will predict the salary for the individual on the basis of his academic and professional profile, and will also indicate the probability of him/her getting placed in an arbitrary company. The interface will also verify the certificates provided by the applicants or students, which makes it easier for the organization to verify the authenticity of the application and student details. 

# Key features 💡
Edurecreuit helps the organization/company to get a better understanding of the candidate’s capabilities and at the same time, it helps the applicant evaluate their skills and apply to the job opportunities according to their capabilities. The explanation of the 3 main features of our application are: 

1. Verification of academic certificates by extracting the verification link provided by the issuing organization. After extracting these details we redirect the recruiter to the verification portal. 
2. Creating prediction of estimated salaries for the applicant according to some parameters filled by the job seeker. We will use a machine learning model to predict the salary and probability of getting selected for a particular job. 
3. Creating a summary of the user’s resume to make it easier for the recruiters to evaluate the applications. 

# Challenges we ran into 🙌
1. Deploying the ML model, integrating the pkl file into the web app
2. Creating a summary of the resume, extracting the text of the user's resume, and creating extractive summary text

# Tech Stack 📚

- HTML, CSS, JavaScript
- Python
- Flask
- Streamlit
- Sklearn, pandas, Numpy
- NLP for summarizer
