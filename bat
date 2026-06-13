#!/bin/bash
bat () {
  VOLTAGE=$(cat $1/voltage_now)
  DESIGN=$(cat $1/energy_full_design)
  FULL=$(cat $1/energy_full)
  NOW=$(cat $1/energy_now)

  HEALTH=$(echo "scale=2; $FULL / $DESIGN * 100" | bc)
  NOW_MAH=$(echo "scale=0; $NOW * 1000 / $VOLTAGE" | bc)
  DESIGN_MAH=$(echo "scale=0; $DESIGN * 1000 / $VOLTAGE" | bc)
  FULL_MAH=$(echo "scale=0; $FULL * 1000 / $VOLTAGE" | bc)
  VOLTS=$(echo "scale=2; $VOLTAGE / 1000000" | bc)

  MFG=$(cat $1/manufacturer)
  MODEL=$(cat $1/model_name)

  echo "Battery $1:"
  echo "  Voltage: $VOLTS V"
  echo "  Design:  $DESIGN_MAH mAh"
  echo "  Full:    $FULL_MAH mAh"
  echo "  Current: $NOW_MAH maH"
  echo "  Health:  $HEALTH%"
  echo "  Part No: $MFG $MODEL"
}

for b in /sys/class/power_supply/BAT* ; do
  bat $b
done


