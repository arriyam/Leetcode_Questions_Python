class Solution:
    def reverse(self, x: int) -> int:

        if len(bin(x)[2:]) <=32:
            x=list(str(x))

            y=x[::-1]

            def int_to_list(z):
                if z[len(z)-1]!='-':
                    if len(z)>9:
                        return(0)

                if z==['0']:
                    return(0)
                while z[0]=='0':
                    z.pop(0)
                z=str(z)
                z = z.replace("[", '')
                z = z.replace("]", '')
                z = z.replace("'", '')
                z = z.replace('"', '')
                z = z.replace(',', '')
                z = z.replace(" ", '')


                if '-' in z:
                    z=z.replace('-','')
                    z=("-"+z)
                    z = z.replace(" ", '')

                    return (z)
                else:

                    return(z)

            return(int_to_list(y))

        else:
            return(0)