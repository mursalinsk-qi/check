package calculator
func Add(num1 int, num2 int) int {
	return num1 + num2
}
func Mul(num1 int, num2 int) int {
	return num1 * num2
}
func Sub(num1 int, num2 int) int {
	if num1 > num2 {
		return num1 - num2
	} else {
		return num2 - num1
	}
}

