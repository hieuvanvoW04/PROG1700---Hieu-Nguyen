"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():

# Input

    EmplyWsalary = float( input( "Please enter the employee's weekly salary: " ) )
    Perdependent = float( input( "How many dependents do you have: " ) )


# Process
    ProvincialTax = 0.06 * EmplyWsalary
    FederalTax = 0.25 * EmplyWsalary
    DependentDeduct= 0.02* Perdependent* EmplyWsalary
    TotalWithheld= ProvincialTax + FederalTax - DependentDeduct
    Totaltakehome = EmplyWsalary - TotalWithheld

# Output
    print("EmplyWsalary: \t$"+format(EmplyWsalary, ",.2f"),"ProvincialTax: \t$"+format(ProvincialTax, ",.2f"),"FederalTax: \t$"+format(FederalTax, ",.2f"),"DependentDeduct: \t$"+format(DependentDeduct, ",.2f"),"TotalWithheld:\t$"+format(TotalWithheld, ",.2f"), \
    "Totaltakehome: \t$" + format( Totaltakehome, ",.2f"),sep = "\n" )


if __name__== "__main__":
    main()
