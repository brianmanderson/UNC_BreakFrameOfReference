from connect import *


def main():
    """
    Note!
    This does not work if the examination has a plan or iso attached to it!

    This will close and open the case, do not panic!
    """
    patient = get_current("Patient")
    patient.Save()
    exam = get_current("Examination")
    exam.AssignToNewFrameOfReference()


if __name__ == '__main__':
    pass