from PolyNode import PolyNode

class Polynomial:
    def __init__(self):
        self.head = None

    # Appending the expression in the polynomial
    def Append(self, coeff, exp):

        new_node = PolyNode(coeff,exp)

        if self.head is None:
            self.head = new_node
        else:
            t = self.head
            while(t.next!=None):
                t = t.next
            t.next = new_node
        
    def display(self):
        temp = self.head
        terms = []
        while temp is not None:
            # Only add terms with non-zero coefficients
            if temp.coeff != 0:
                if temp.exp == 0:
                    terms.append(f"{temp.coeff}")
                elif temp.exp == 1:
                    terms.append(f"{temp.coeff}x")
                else:
                    terms.append(f"{temp.coeff}x^{temp.exp}")
            temp = temp.next
        return " + ".join(terms) if terms else "0"

poly = Polynomial()

poly.Append(3,2)
poly.Append(2,1)
poly.Append(8,0)

expression = poly.display()
print(expression)
