# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
#    (Also clean the input so it becomes either 'Y' or 'N'.)
medical_cause=input( 'Do you have amedical cause' ).lower()
if (medical_cause  == 'y'):
    print('you are aollwed')
else:
    atten=int(input('Enter the atten'))
    if ( atten>=75):
     print('aollwed')
    else: 
       print('not aollwed')
# 2) If `medical_cause` is 'Y':
#    - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):
#    a) Ask for the student’s attendance percentage and store it in `atten`.
#    b) If `atten` is 75 or more:
#       - Print "Allowed"
#    c) Else:
#       - Print "Not allowed"