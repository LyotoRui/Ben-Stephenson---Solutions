plate = input('Enter the license plate: ').upper()

if len(plate) == 6 and 'A' <= plate[0] <= 'Z' and \
    'A' <= plate[1] <= 'Z' and 'A' <= plate[2] <= 'Z' and \
    '0' <= plate[3] <= '9' and '0' <= plate[4] <= '9' and \
    '0' <= plate[5] <= '9':
    print('This is valid for the old plate style.')
elif len(plate) == 7 and  '0' <= plate[0] <= '9' and \
    '0' <= plate[1] <= '9' and '0' <= plate[2] <= '9' and \
    '0' <= plate[3] <= '9' and 'A' <= plate[4] <= 'Z' and \
    'A' <= plate[5] <= 'Z' and 'A' <= plate[6] <= 'Z':
        print('This is valid for the new plate style.')
else:
    print('This license plate is invalid.')