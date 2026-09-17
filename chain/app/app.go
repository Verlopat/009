package app

type App struct {
	Name string
}

func NewApp() *App {
	return &App{Name: "vec"}
}
