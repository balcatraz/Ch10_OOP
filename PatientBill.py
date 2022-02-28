import PatientClass as pt
import ProcedureClass as pr

def main():
    newPatient = pt.Patient(1, 'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', True)
    proced1 = pr.Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1)
    proced2 = pr.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
    proced3 = pr.Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2)

    print('*** Patient Bill ***')
    print('Name:', newPatient.getName())
    print('Address:', newPatient.getAddress())
    print('Phone:', newPatient.getPhNum())
    print()

    print('Procedure:', proced1.getName())
    print('Date:', proced1.getDate())
    print('Practitioner:', proced1.getPractitioner())
    print('Charge:', "${:,.2f}".format(proced1.getCharge()))
    print()

    print('Procedure:', proced2.getName())
    print('Date:', proced2.getDate())
    print('Practitioner:', proced2.getPractitioner())
    print('Charge:',"${:,.2f}".format(proced2.getCharge()))
    print()

    procList = [proced1,proced2,proced3]

    totalCharge = 0
    for a in procList:
        if a.getPtID() == 1:
            totalCharge += a.getCharge()

    if newPatient.getVetStatus():
        totalCharge *= .6

    print('Total Charges:', "${:,.2f}".format(totalCharge))

main()