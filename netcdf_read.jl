using NCDatasets

fl = "test-data/OR_ABI-L1b-RadF-M6C13_G16_s20221502300204_e20221502309524_c20221502309585.nc"

function get_xy(fn::String)::NamedTuple
    ds = Dataset(fn)
    return (x=ds["x"][:,:], y=ds["y"][:,:])
end


function example_fct(a::Float32, b::Float32)::Float32
    return sin(a) + 2 * b^2 / cos(a+b)
end

xy = get_xy(fl)

z = [example_fct(x, y) for x in xy.x, y in xy.y]

maximum(z)
