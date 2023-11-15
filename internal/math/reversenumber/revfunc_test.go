package reversenumber

import (
	"github.com/stretchr/testify/assert"
	"io"
	"os"
	"testing"
)

func TestReverse(t *testing.T) {
	var tests = []struct {
		a    int
		want int
	}{
		{30, 03},
		{-1, 0},
		{0, 0},
		{11, 11},
		{89848, 84898},
	}
	for _, val := range tests {
		result := ReverseNumber(val.a)
		assert.Equal(t, val.want, result, "Not equal")
	}
}

func TestHello(t *testing.T) {
	oldOut := os.Stdout
	r, w, _ := os.Pipe()
	os.Stdout = w
	Hello()
	_ = w.Close()
	os.Stdout = oldOut
	out, _ := io.ReadAll(r)
	if string(out) != "HELLO" {
		t.Errorf("Incorrect Value. received %s", string(out))
	}
}
