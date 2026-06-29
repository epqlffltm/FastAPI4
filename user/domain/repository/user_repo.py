#user/domain/repository/user_repo.py

from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self,user: User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email:str)->User:
        """
        이메일로 유저를 검색, 유저가 없다면 422 애러를 발생시킨다.
        """
        raise NotImplementedError