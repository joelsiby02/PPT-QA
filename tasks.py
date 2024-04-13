from textwrap import dedent
from crewai import Task

class ProjectSelectionTask:
    def question_task(self, agent, pdf):
        general_questions = [
            "What are the tools used?",
            "Why choose this specific tool?",
            "Why choose X tool instead of the alternative Y?",
            "What could be the expected accuracy score of the model?",
            "What ML/DL algorithm are you using to classify?",
            # Additional general questions
            "How does the chosen tool/methodology contribute to solving the problem statement?",
            "Can you elaborate on the decision-making process behind selecting this specific tool?",
            "What are the potential challenges or limitations associated with the chosen approach?",
            "How do you plan to address potential biases or inaccuracies in the data?",
            "Can you discuss any ethical considerations relevant to your project?",
            "What are the implications of your findings for real-world applications?",
            "How does your work contribute to existing research in the field?",
            "Can you explain any assumptions made during the project and their impact on the results?",
            "How do you plan to evaluate the performance of your model or solution?",
            "Can you discuss any future directions or extensions for this work?"
        ]

        general_questions_text = "\n".join([f"- {q}" for q in general_questions])

        return Task(
            description=dedent(f"""\
                You will be responsible for creating 5 general and 5 intermediate questions and answers based on the inputted text or pdf forwarded to you. The answer generated should be extracted from the vector database to check if it is accurate.
                Use tool only if nessasary
                Input PDF or text:
                ------------
                {pdf}

                Additional General Questions:
                {general_questions_text}
            """),
            async_execution=True,
            agent=agent,
            expected_output='''
            Your Final answer should maintain the format of 5 general questions and 5 intermediate questions classified into a format, questions in points and below you should output the answers from the pdf and nothing else. It's mandatory to return only the questions and answers and nothing else and also keep a generic format. Each iteration should output different questions, and the results should be sent to the next task.
        Return no ticks or 'Here are your answers' like text only general and intermediate questions along with their answers from the pdf or generate responce as simple as possible
        '''
        )

    def valuation_task(self, agent, pdf):
        return Task(
            description=dedent(f"""\
                Your job is to verify the questions created from the inputted pdf or text and nothing else, no outside questions. 
                Also, you should be verifying that the answers created are within or similar to the right information within the pdf or text.
                Use tool only if nessasary
                Input PDF or text:
                ------------
                {pdf}

                Your Final answer should maintain the format of questions in points and below that, answers from the pdf and nothing else. It's mandatory to return only the questions and answers and nothing else and also keep a generic format.
            """),
            agent=agent,
            expected_output="Your Final answer should maintain the format of 5 general questions and 5 intermediate questions classified into a format, questions in points and below that, answers from the pdf and nothing else. It's mandatory to return only the questions and answers and nothing else and also keep a generic format. Each iteration should output different questions."
        )
