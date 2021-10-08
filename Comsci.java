class Comsci
{
    String name, year, course, subject;
    
    Comsci()
    {
        name = "Jessie Apac";
        year = "2nd Year 21A1";
        course = "Bachelor of Science in Computer Science";
    }

    public void ALL()
    {
        this.createBlock(1, 100);
        this.studentInfo();
        this.createBlock(1, 100);
        this.reportCard();
        this.createBlock(1, 100);
    }

    public void setName(String aname) //NO Middle name //First bigletter for every firstname or second etc and surname
    {
        //Firstname Secondname Surname
        if(aname == "Ayo Miguel Repaso")
        {
            name = aname;
        }
        else if(aname == "David Dwaight Tayco")
        {
            name = aname;
        }
    }
    public void studentInfo()
    {
        System.out.println("Student Name: " + name);
        System.out.println("Student Yr&Sec: " + year);
        System.out.println("Student Course: " + course);

    }
    public void reportCard()
    {
        System.out.println("                                        Report Card                                        ");
        subject = "CC213     Data Structures and Algorithm     Mon     12:00-03:30PM     9/10";
        System.out.println(subject);
        subject = "GEC10     Art Appreciation                  Mon     04:00-06:00PM     5/10";
        System.out.println(subject);
        subject = "DS213     Discrete Structures 2             Tue     01:30-03:30PM     6/10";
        System.out.println(subject);
        subject = "SDF213    Object Oriented Programming       Wed     06:30-08:00PM     10/10";
        System.out.println(subject);
        subject = "GEC101    Purposive Communication           Wed     04:00-06:00PM     4/10";
        System.out.println(subject);
        subject = "PE103     Physical Fitness 3                Fri     10:00-12:00NN     0/10";
        System.out.println(subject);
        subject = "GAD213    2D Game Art Development           Fri     01:00-04:30NN     4/10";
        System.out.println(subject);
        subject = "SDF213    Object Oriented Programming       Fri     05:00-07:00PM     10/10";
        System.out.println(subject);
        subject = "CC213     Information Management            Sat     08:00-11:30AM     7/10";
        System.out.println(subject);
    }
    public void students()
    {
        System.out.println("1. Ayo Miguel Repaso");
        System.out.println("2. David Dwaight Tayco");
        System.out.println("3. Jessie Apac");
    }
    public void createBlock(int row, int column)
    {
        for(int i = 1;i <= row;i++)
        {
            for(int j = 1; j <= column; j++)
            {
                System.out.print("=");
            }
            System.out.println("");
        }
    }
}