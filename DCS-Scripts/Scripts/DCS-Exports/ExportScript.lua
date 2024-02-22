local default_output_file = nil

function LuaExportStart()
    package.path = package.path .. ";" .. lfs.currentdir() .. "/LuaSocket/?.lua"
    package.cpath = package.cpath .. ";" .. lfs.currentdir() .. "/LuaSocket/?.dll"
    socket = require("socket")
    host = host or "192.168.2.102"
    port = port or 7777
    connection = socket.udp()
    connection:setpeername(host, port)
end

function LuaExportBeforeNextFrame()
end

function LuaExportAfterNextFrame()
end

function LuaExportStop()
    socket.try(c:send("quit"))
    connection:close()
end

function LuaExportActivityNextEvent(t)
    local tNext = t

    local aoa = LoGetAngleOfAttack() -- (rad)
    local accelerations = LoGetAccelerationUnits() -- ({x = Nx,y = NY,z = NZ} 1 (G)) x-nose(-)/tail(+) y-up(-)/down(+) z-left(-)/right(+)
    local ias = LoGetIndicatedAirSpeed() -- (m/s)
    local vvert = LoGetVerticalVelocity() -- (m/s)
    local altBar = LoGetAltitudeAboveSeaLevel() -- (m)

    socket.try(connection:send(
         string.format(
            "%.2f,%.2f,%.2f,%.2f,%.1f,%.1f,%.1f",
            aoa,
            accelerations["x"],
            accelerations["y"],
            accelerations["z"],
            vvert,
            ias,
            altBar
        )
    ))
    -- '3.23,0.19,0.02,0.03,-53.9,45.7,4407.6' example

    tNext = tNext + .16
    return tNext
end
