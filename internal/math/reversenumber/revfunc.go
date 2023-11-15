package reversenumber

import "fmt"

func ReverseNumber(num int) int {
	res := 0
	for num > 0 {
		remainder := num % 10
		res = (res * 10) + remainder
		num /= 10
	}
	return res
}

func Hello() {
	fmt.Print("HELLO")
}
