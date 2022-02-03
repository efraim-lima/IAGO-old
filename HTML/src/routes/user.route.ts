import { Request, Response, NextFunction, Router } from "express";
import { StatusCodes } from 'http-status-codes'
// get /users
// get /users/:uuid
// post /users
// put /users/:uuid
// delete /users/:uuid

const usersRout = Router()

usersRout.get('/users', (req: Request, res: Response, next: NextFunction) => {
    const users = [{
        userName: 'Efraim'
    }]
    res.status(StatusCodes.OK).send(users)
})

usersRout.get('/users/:uuid', (req: Request, res: Response, next: NextFunction) => {
    const uuid = req.params.uuid
    //bancoDeDados.getUserByUuid(uuid)
    res.status(StatusCodes.OK).send({uuid})
})

usersRout.post('/users', (req: Request, res: Response, next: NextFunction) => {
    const newUser = req.body
    res.status(StatusCodes.CREATED).send(newUser)
})

usersRout.put('/users/:uuid', (req: Request, res: Response, next: NextFunction) => {
    const uuid = req.params.uuid
    //bancoDeDados.getUserByUuid(uuid)
    const modifiedUser = req.body
    modifiedUser.uuid = uuid
    res.status(StatusCodes.OK).send({modifiedUser})
})

usersRout.delete('/users/:uuid', (req: Request, res: Response, next: NextFunction) => {
    res.sendStatus(StatusCodes.OK)
})

export default usersRout