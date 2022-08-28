

#THIS IS WHAT MAKES THE EMAIL MACHINE FUNCTIONAL. EVERYTHING FROM HERE TO THE END COMMENT CAN BE COPY, PASTED AND MODIFIED FOR YOUR OWN EMAIL MACHINE PROJECT IF NEEDED!#
import smtplib
import os
import sys

def emailMechanism():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection: 
            print("\n#--------------------------------------#\n")
            clientEmail=input('Please input client email here: ')  #THIS IS THE RECIEVER EMAIL ADDRESS!#
         
            email_address = 'YourEmail@gmail.com' #THIS IS YOUR (BUSINESSES) EMAIL ADDRESS!
            email_password = 'n/a' #USE YOUR EMAIL ACCOUNTS APP PASSWORD HERE TO GET PROGRAM RUNNING! REPLACE "n/a" WITH SAID  APP PASSWORD!#
            connection.login(email_address, email_password )
            connection.sendmail(from_addr=email_address, to_addrs=clientEmail, 
                msg="subject: LockSplitr.com: Your Report Is Ready! \n\n "  + f + "") #VARIABLE "f" IS WHATEVER VARIABLE/STRING THAT YOU WANT TO SEND. BELOW YOUR DESIRED STRING BELOW, TYPE "f= *Given String* " TO MAKE THIS WORK FOR YOUR OWN NEEDS!
                    #EVERYTHING AFTER "Subject:" CAN BE DELETED AND REPLACED WITH YOUR OWN CUSTOM SUBJECT LINE!#
                    
            print("Sending Email....")
            print("\n#--------------------------------------#\n")
            print("Email Sent!")
          


def satisfactory():
    print("\n\n#--------------------#\n\n")
    satisfactory1=input("Is this satisfactory (y/n): ")
    if satisfactory1 == "y":
        emailMechanism()
        
    if satisfactory1 == "n":
        print("\n\n#----------RESTARTING PROGRAM----------#\n\n")
        os.execl(sys.executable, sys.executable, *sys.argv)

def finalEmail():
    print ("\n\n#----------Here is your final email:----------#\n\n ")

#END COMMENT#

#EVERYTHING BEYOND HERE CAN BE MODIFIED TO FIT YOUR OWN NEEDS, AND MODIFY YOUR  EMAIL SENDING PROCESS IN A SIMILAR FASHION!#

#EVERYTHING ABOVE THIS I RECCOMEND KEEPING FOR YOUR OWN PROGRAMS FUNCTIONALITY, AS IT MOSTLY PERTAINS TO THE ACTUAL FUNCTIONALITY OF THE EMAIL MACHINE ITSELF. MOST EVERYTHING BELOW CAN BE MODIFIED. PLEASE MAKE YOURSELF AWARE OF THE VARIABLES ABOVE (AND I ALSO RECCOMENDED IN THIS GENERAL PROGRAM) TO HELP MAKE YOUR CODING EXPERIENCE EASIER!#

footer="\n\nSincerely,\n\nLockSplitr.com Team\n\n" #CUSTOMIZE THE FOOTER TO YOUR NEEDS!
print("\n#--------------------------------------#\n")
clientName=input("Hello! To get started, please input the clients name here: ")
print(clientName)
clientInfo=("Dear " + clientName + ", \n")

servicePicker=input('Is this email for a cellular unlocking? (y/n): ')
print(servicePicker)

if servicePicker == "y":
        successfulUnlock=input("Was the unlocking successful? (y/n): ")
        if successfulUnlock == "n":
            unsuccessfulUnlock= "\n We regret to inform you that your device was unable to be successfully unlocked for the following reasons: "

            unsuccessfulReason=input("Input the reasons sited here: ")
            refund=input("Is this order eligible for a refund? (y/n): ")
            if refund == "y":
                yesRefund = "\nGiven that this order does not breach any of the stated reasonings on our Terms and Conditions page, you are entitled to a full refund on our behalf. We thank you for your business! "

                print('Here is your final e-mail: \n' +clientInfo + unsuccessfulUnlock + unsuccessfulReason+ yesRefund + footer +"")
                
                unsuccUnsuccYesRef=("" +clientInfo + unsuccessfulUnlock + unsuccessfulReason + yesRefund + footer + "")
                f=unsuccUnsuccYesRef
                satisfactory() #END ALL SUCCESSFUL EMAIL PROMPTS/STATEMENTS WITH "satisfactory()", AS SHOWN!

            if refund == "n":
                noRefund = "\n \n Given the reasons listed on our websides Terms and Conditions page, your order will not be refunded for this service, with this decision being final. we are sorry for any distress that this may cause, and thank you for your business. "
                print ("Here is your final email: \n" +clientInfo + unsuccessfulUnlock + unsuccessfulReason + noRefund + footer + "")
                
                unsuccUnsuccNoRef=("" +clientInfo + unsuccessfulUnlock + unsuccessfulReason + noRefund + footer + "")
                f=unsuccUnsuccNoRef
                satisfactory()#END ALL SUCCESSFUL EMAIL PROMPTS/STATEMENTS WITH "satisfactory()", AS SHOWN!

        if successfulUnlock == "y":
            successfulUnlockString= "\n Congratulations! your mobile device has been successfully unlocked!"
            unlockCode=input("Does this order require an UNLOCK CODE?: ")
            if unlockCode == "y":
                unlockCodeYes=input("Please input unlock code here: ")
                unlockCodeString=('\nHere is your devices unlock code: ' +unlockCodeYes)
                unlockCodeSteps="\n\nTo unlock your device, please follow the following steps: \n\n 1. Power off your device \n 2. Insert alternative carrier SIM card into your device. \n 3. Power device on \n 4. Wait for device to display *SIM Network unlock PIN* screen \n 5. Enter the given code provided and then tap UNLOCK \n 5. Congratulations! Your device should now be fully unlocked! "
        
                successYesCode=("" +clientInfo + successfulUnlockString + unlockCodeYes + unlockCodeString+ unlockCodeSteps + footer + "")
                print ("Here is your final email: \n" + successYesCode + "")
                f=successYesCode
                satisfactory()#END ALL SUCCESSFUL EMAIL PROMPTS/STATEMENTS WITH "satisfactory()", AS SHOWN!



            if unlockCode == "n":
                unlockCodeNo="\n\nAfter our analysis of your phones IMEI, we have determined that this given cellular unlocking does not require an unlock code. To complete this process, please reset your device and put in your new SIM card to see the changes in effect. \n\n We thank you for your business!"
                
                successNoCode=("" +clientInfo + successfulUnlockString + unlockCodeNo + footer + "")
                print ("Here is your final email: \n" + successNoCode + "")
                f=successNoCode
        
                satisfactory() #END ALL SUCCESSFUL EMAIL PROMPTS/STATEMENTS WITH "satisfactory()", AS SHOWN!
                

if servicePicker == 'n':
        imeiInfo="The results of your IMEI Info Report are here: \n\n"
        print('\n\n#----------please input the following information:----------#\n\n')

        model=input("\nModel: \n")
        imeiGeneral=input("\nIMEI: \n")
        serialNum=input("\nSerial: \n")
        carrier=input("\nCarrier: \n")
        country=input("\nCountry: \n")
        simLock=input("\nSIM Lock: \n")
        findMyIphone=input("\nFind My iPhone: \n")
        icloud=input("\niCloud Status: \n")
        blacklist=input("\nBlacklisted: \n")
        manufactureDate=input("\nDate of Manufacture: \n")
        additional=input("\nAdditional Information: \n")

        ImeiExit='\n We thank you for your business!'

      
        
        introChecker=(""+clientInfo+imeiInfo+"\n")
        model2=("Model: " + model + '\n')
        imei2=("\nIMEI: " + imeiGeneral + '\n')
        serial2=("\nSerial: " + serialNum + '\n')
        carrier2=("\nCarrier: " + carrier + '\n')
        country2=("\nCountry: " + country + '\n')
        sim=("\nSIM Lock: " + simLock + '\n')
        findIphone=("\nFind My iPhone: " + findMyIphone + '\n')
        icloudLock=("\niCloud Status: " + icloud + '\n')
        bl=("\nBlacklisted: " + blacklist + '\n')
        manDate=("\nDate of Manufacture: " + manufactureDate + '\n')
        addInf=("\nAdditional Information: " + additional + '\n')
        exit=(""+ImeiExit+footer+"")
        
       
        
        imeiInfoCheckerString=(""+introChecker+model2+imei2+serial2+carrier2+country2+sim+findIphone+icloudLock+bl+manDate+addInf+exit+"")
        f=imeiInfoCheckerString
        print ("Here is your final email: \n" + imeiInfoCheckerString + "")
        satisfactory() #END ALL SUCCESSFUL EMAIL PROMPTS/STATEMENTS WITH "satisfactory()", AS SHOWN!

