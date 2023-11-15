package wordcounter

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestCount(t *testing.T) {
	var testcase = []struct {
		str  string
		want int
	}{
		{"Hell", 4},
		{" ", 1},
		{"", 0},
	}
	for _, val := range testcase {
		result := Wordc(val.str)
		assert.Equal(t, val.want, result, "Not correct count")
	}
}
