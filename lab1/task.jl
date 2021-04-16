using CSV
using DataFrames
using Dates


df = DataFrame(CSV.File("task1.csv", dateformat= "m/d/y"))

df2 = DataFrame(CSV.File("task1.csv", dateformat= "hh:mm:ss"))

df.Data_fim = Date.(df.Data_fim, "mm-dd-yyyy")