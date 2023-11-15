package calculator

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAdd(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{30, 40, 70},
		{-1, -5, -6},
		{0, 0, 0},
		{15, -4, 11},
	}
	for _, val := range tests {
		result := Add(val.a, val.b)
		assert.Equal(t, val.want, result, "Not equal")
	}
}

func TestMul(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{30, 40, 1200},
		{-1, -5, 5},
		{0, 4654, 0},
		{15, -4, -60},
	}
	for _, val := range tests {
		result := Mul(val.a, val.b)
		assert.Equal(t, val.want, result, "Not equal")
	}
}
func TestSub(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{30, 40, 10},
		{40, 30, 10},
		{0, 4654, 4654},
		{15, -30, 45},
		{-50, -30, 20},
	}
	for _, val := range tests {
		result := Sub(val.a, val.b)
		assert.Equal(t, val.want, result, "Not equal")
	}
}