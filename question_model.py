class Question:
    '''this is used to create question objects to put into the question bank which is just an array
    of these objects. The objects are made by a question and its answer'''
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
