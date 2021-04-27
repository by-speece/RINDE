killall polybar

killall -q polybar


while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done


polybar bottom -c ~/.config/polybar/config.ini &
polybar top  -c ~/.config/polybar/config.ini &
