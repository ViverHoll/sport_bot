# from typing import Optional, Any
#
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.models.sql import SportFoodModel
# from app.db.repository import Repository
# from app.models.dataclasses import SportFood
#
#
# class SportFoodDAO:
#     repository: Repository[SportFoodModel]
#
#     __slots__ = ("repository",)
#
#     def __init__(self, *, session: AsyncSession) -> None:
#         self.repository = Repository(
#             session=session,
#             model=SportFoodModel,
#         )
#
#     async def add_sport_food(self, **values: Any) -> None:
#         await self.repository.insert(**values)
#         await self.repository.commit()
#
#     async def get_sport_food_by_id(self, food_id: int) -> Optional[SportFood]:
#         result_obj = await self.repository.get_by_where(
#             SportFoodModel.id == food_id,
#         )
#         food = result_obj.all()
#         if food:
#             return SportFood(*food[0])
#         return None
#
#     async def get_all_sport_foods(self) -> list[SportFood]:
#         result_obj = await self.repository.get_by_where()
#         sport_foods = result_obj.all()
#
#         if sport_foods:
#             return [
#                 SportFood(*food)
#                 for food in sport_foods
#             ]
#         return []
