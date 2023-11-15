package main
import (
	"fmt"
	"go-tutorails/internal/math/wordcounter"
)
func main() {
	var st string
	fmt.Println("Enter a word to count number of letters")
	fmt.Scanf("%s", &st)
	res := wordcounter.Wordc(st)
	fmt.Printf("The number of letters present  is %d\n", res)
}
