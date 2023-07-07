#PRG-1000

#Billånskalkulator
#Innhente informasjon fra brukeren for å videre beregne om brukeren valideres for lån.
#Programmet skal kunne kjøres igjen om ønskelig.
#Programmet skal beregne egenkapitalandel, terminbeløp og det som ventes ved en lånesøknad.

#Car loan calculator
#Gathers information from user for calculating if the user can get a loan
#The program should be able to run as the user want to check for loans.
#The program must calculate equity, term amount and whats crucial for a loan application.

#Lager en variabel for å kontrollere loopen
#Creating a variabel for controlling the loop
start_pa_nytt='j'

while start_pa_nytt=='j':

#Starter med å innhente informasjon fra brukeren hva gjelder verdier
#Gathers information from the user, carprice, downpaymenttime, equity
#Setting the annual interest to 0
    
    bil_pris=float(input('Oppgi bilens pris: '))
    nedbetalingstid=float(input('Oppgi ønsket nedbetalingstid: '))
    egenkapital=float(input('Oppgi din egenkapital: '))
    arlig_rente=0
    
#Utregning av egenkapitalprosent
#Calculation of the equity percentage

    egenkapital_prosent=((egenkapital)/(bil_pris))
    print()
    print('Resultatet av egenkapitalprosenten er:',egenkapital_prosent)
    print()
    
#Sjekker om brukeren har nødvendig egenkapital
#Checking wether the user have the right amount of equity

    if egenkapital_prosent>0.35:
        if egenkapital_prosent<0.50:
            arlig_rente=0.045
            print('Din årlige rentesats vil være 4,5%')
        else:
            if egenkapital_prosent<0.60:
                arlig_rente=0.03
                print('Din årlige rentesats vil være 3%')
            else:
                if egenkapital_prosent>=0.60:
                    arlig_rente=0.025
                    print('Din årlige rentesats vil være 2,5%')
                else:
                    print('Du trenger ikke lån')


#Om egenkapital er godkjent går vi videre til avsluttende del som angår terminbeløp
#If equity is approved, proceed to finalizing and term amount

        lanebelop=(bil_pris-egenkapital)
        terminrente=(arlig_rente/12)
        antall_terminer=(nedbetalingstid*12)
        terminbelop=lanebelop*(((1+terminrente)**antall_terminer)*terminrente/(((1+terminrente)**antall_terminer)-1))

#Oversikt over lån med print
#Prints with overview of the loan
        
        print('Ønsket lånebeløp er:',lanebelop,'kr')
        print()

        print('Ønsket nedbetalingstid er:',nedbetalingstid,'år')
        print()

        print('Årlig rente blir:',arlig_rente,'kr')
        print()

        print('Terminrenten blir: ''kr',terminrente)
        print()

        print('Terminbeløp pålydende:',format(terminbelop,'.2f'))
        print()

        print('Kalkulator avsluttet')

    else:
        print('Du har dessverre ikke nok egenkapital for å få innvilget lånet')



    
    start_pa_nytt=input('Vil du starte kalkulatoren på nytt?'+'(Tast "j" for ja): ')    

#Program slutt
#Program ends
