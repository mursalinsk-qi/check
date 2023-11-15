package main
import (
	"fmt"
	"go-tutorails/internal/math/reversenumber"
)
func main() {
	fmt.Println("Enter the number")
	var ele int
	fmt.Scanf("%d\n",& ele)
	result:=reversenumber.ReverseNumber(ele)
	fmt.Println(result)
}
