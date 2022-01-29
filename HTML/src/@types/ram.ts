const os = require('os')


setInterval (() => {
    const {arch, platform, totalmem, freemem} = os
    const tRam = parseInt(totalmem()/1024/1024)
    const fRam = parseInt(freemem()/1024/1024)
    const Usage = (fRam/tRam)*100
    
    const stats = {
        OS: platform(),
        Arch: arch(),
        RAM: `${tRam}MB`,
        Free: `${fRam}MB`,
        Usage: `${Usage.toFixed()}%`

    }
    console.clear()
    console.table(stats)
    exports.stats = stats
}, 1000)
