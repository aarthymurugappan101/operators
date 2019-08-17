number = 5
usrInput = input("Enter a number? ")
usrInput = int(usrInput)
# print("Is your number greater than 5?", usrInput > number)
                            #  not     FALSE
print("Is this opposite?", not usrInput > number)

                                                        #    TRUE      and TRUE  -> given number is 7
                                                        #    TRUE      and FALSE  -> given number is 11
# print("Is the number greater than 5 and lesser than 10?", usrInput > 5 and usrInput < 10)


                                                        #    TRUE    or TRUE  -> given number is 7
                                                        #    TRUE    or FALSE  -> given number is 11
# print("Is the number greater than 5 or greater than 10?", usrInput > 5 or usrInput > 10)