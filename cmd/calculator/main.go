package main
import (
	"fmt"
	"go-tutorails/internal/math/calculator"	
)
func main() {
	fmt.Println("Press\n 1:add \n 2:Multiply \n 3:Difference")
	var choice int
	fmt.Scanf("%d\n", &choice)
	fmt.Println("Enter two number")
	var val1, val2 int
	fmt.Scanf("%d\n", &val1)
	fmt.Scanf("%d\n", &val2)
	if choice == 1 {
		res := calculator.Add(val1, val2)
		fmt.Println("The Addition value is", res)
	} else if choice == 2 {
		res := calculator.Mul(val1, val2)
		fmt.Println("The Multiplication value is", res)
	} else {
		res := calculator.Sub(val1, val2)
		fmt.Println("The Difference value is", res)
	}
	
	
}
