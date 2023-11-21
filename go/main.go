package main

import (
	"errors"
	"fmt"
	"math"
	"time"

	"github.com/goccy/go-json"

	"github.com/gin-gonic/gin"
)

type FigureInterface interface {
	GetType() string
	ComputeArea() float64
}

type Figure struct {
	Type string `json:"type"`
}

type Square struct {
	Figure
	Size uint32 `json:"size"`
}

type Rectangle struct {
	Figure
	SizeA uint32 `json:"sizeA"`
	SizeB uint32 `json:"sizeB"`
}

type Triangle struct {
	Figure
	SizeA uint32 `json:"sizeA"`
	SizeB uint32 `json:"sizeB"`
	SizeC uint32 `json:"sizeC"`
}

type Circle struct {
	Figure
	Diameter uint32 `json:"diameter"`
}

func (f Figure) GetType() string {
	return f.Type
}

func (f Square) ComputeArea() float64 {
	return float64(math.Pow(float64(f.Size), 2))
}

func (f Rectangle) ComputeArea() float64 {
	return float64(f.SizeA * f.SizeB)
}

func (f Triangle) ComputeArea() float64 {
	a := float64(f.SizeA)
	b := float64(f.SizeB)
	c := float64(f.SizeC)
	s := (a + b + c) / 2

	return math.Sqrt(s * (s - a) * (s - b) * (s - c))
}

func (f Circle) ComputeArea() float64 {
	radius := float64(f.Diameter) / 2
	return math.Pi * (math.Pow(radius, 2))
}

func loadFigures() []FigureInterface {
	var rawFigures []json.RawMessage
	json.Unmarshal([]byte(FIGURES), &rawFigures)

	figures := make([]FigureInterface, 0, 500)

	for _, raw := range rawFigures {
		var tmp Figure
		json.Unmarshal(raw, &tmp)

		var figure FigureInterface

		switch tmp.Type {
		case "square":
			figure = &Square{}
			break
		case "rectangle":
			figure = &Rectangle{}
			break
		case "triangle":
			figure = &Triangle{}
			break
		case "circle":
			figure = &Circle{}
			break
		default:
			panic(errors.New("Unsupported figure type"))
		}

		json.Unmarshal(raw, figure)
		figures = append(figures, figure)
	}

	return figures
}

func main() {
	r := gin.New()

	r.GET("/ping", func(c *gin.Context) {
		figures := loadFigures()

		var minArea float64 = math.MaxFloat64
		var maxArea float64 = 0.0
		var totalArea float64 = 0.0
		var figuresCount = make(map[string]uint32)

		for _, figure := range figures {
			area := figure.ComputeArea()
			minArea = math.Min(minArea, area)
			maxArea = math.Max(maxArea, area)
			totalArea += area
			figuresCount[figure.GetType()]++
		}

		c.JSON(200, gin.H{
			"app":          "go-gin****",
			"time":         time.Now().Unix(),
			"min_area":     minArea,
			"max_area":     maxArea,
			"total_area":   totalArea,
			"figure_types": figuresCount,
		})
	})

	r.POST("/ping", func(c *gin.Context) {
		figures := loadFigures()

		var minArea float64 = math.MaxFloat64
		var maxArea float64 = 0.0
		var totalArea float64 = 0.0
		var start = time.Now().UnixMilli()

		for i := 1; i <= 1_000_000; i++ {
			for _, figure := range figures {
				area := figure.ComputeArea()
				minArea = math.Min(minArea, area)
				maxArea = math.Max(maxArea, area)
				totalArea += area
			}
		}

		c.JSON(200, gin.H{
			"app":        "go-gin****",
			"time":       time.Now().UnixMilli() - start,
			"min_area":   minArea,
			"max_area":   maxArea,
			"total_area": totalArea,
		})
	})

	fmt.Println("Server started at 0.0.0.0:8080")
	r.Run("0.0.0.0:8080")
}
