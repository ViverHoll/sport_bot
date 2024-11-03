# from typing import Optional, Any
#
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.db.repository import Repository
# from app.models.sql import SocialNetworkModel
# from app.models.dataclasses import SocialNetworkType
#
#
# class SocialNetworkDAO:
#     repository: Repository[SocialNetworkModel]
#
#     __slots__ = ("repository",)
#
#     def __init__(self, session: AsyncSession) -> None:
#         self.repository = Repository(
#             session=session,
#             model=SocialNetworkModel,
#         )
#
#     async def add_user(
#             self,
#             *,
#             user_id: int,
#             full_name: str,
#             age: int,
#             media: str,
#             city: str,
#             description: str,
#             likes: int = 0,
#     ) -> None:
#         await self.repository.insert(
#             user_id=user_id,
#             full_name=full_name,
#             age=age,
#             media=media,
#             city=city,
#             description=description,
#             likes=likes,
#         )
#         await self.repository.commit()
#
#     async def get_user_by_id(self, user_id: int) -> Optional[SocialNetworkType]:
#         result_obj = await self.repository.get_by_where(
#             SocialNetworkModel.user_id == user_id,
#         )
#         user = result_obj.all()
#         if user:
#             return SocialNetworkType(*user[0])
#         return None
#
#     async def update_user(self, user_id: int, **values: Any) -> None:
#         await self.repository.update_by_where(
#             SocialNetworkModel.user_id == user_id,
#             **values,
#         )
#         await self.repository.commit()
