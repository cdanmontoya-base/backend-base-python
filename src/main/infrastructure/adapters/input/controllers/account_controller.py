from fastapi import APIRouter
from dataclasses import dataclass
from injector import inject

from src.main.application.services.insert_account_service import InsertAccountService


class AccountController:
    router: APIRouter
    insert_account_service: InsertAccountService

    @inject
    def __init__(self, insert_account_service=None) -> None:
        self.router = APIRouter(
            prefix='/accounts',
            tags=['accounts'],
            responses={404: {'description': 'Not found'}}
        )
        self.insert_account_service = insert_account_service

        self.router.add_api_route('/', self.get_all, methods=['GET'])
        self.router.add_api_route('/', self.insert, methods=['POST'])

    @staticmethod
    async def get_all():
        return "get all"

    async def insert(self):
        return self.insert_account_service.insert('whom')
