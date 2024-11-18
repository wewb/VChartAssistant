### Background​
VisActor is a data visualization rendering engine that has won the love of many front-end developers in the open source community. You are a development contributor of the VChart framework in the VisActor project. Every day, many users ask you questions about the use of the warehouse. In order to reduce the burden of operating open source projects and better serve users, you hope to develop an intelligent question and answer robot with the help of LLM + LangChain. The robot can answer users' frequently asked questions based on the user documentation of the open source project.

https://github.com/VisActor/VChart/tree/develop

### Requirements description​
The VChart intelligent question and answer robot needs to provide a visual interactive interface for developers to use when they encounter problems. Typical user questions are as follows:​
1. Framework introduction class: Introduce the VChart chart and what parts it consists of.
2. Function usage category: How to download VChart? How to use VChart to configure a correlation scatter plot?​
3. Scenario consultation: I find that if the number has a long decimal point, it looks unsightly. Is there any way to control the length of the decimal place displayed on the label?​

The system needs to refer to the content in user documents, locate the most relevant information and generate corresponding answers through large models. If necessary, it can output multi-modal data such as code/pictures to better answer user questions.

