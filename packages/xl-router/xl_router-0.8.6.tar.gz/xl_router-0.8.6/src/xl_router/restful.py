from typing import Optional


class R:
    @classmethod
    def get(cls, 
            id: Optional[int] = None, 
            order_key: Optional[str] = 'id', 
            order_way: Optional[str] = 'desc',
            page_num: Optional[int] = None, 
            page_size: Optional[int] = None, 
            **kwargs):
        if id:
            return cls.get_json(id)
      
        else:
            order_by = {order_key: order_way} if order_key else {}
            params = getattr(cls, 'params', []) 
            kwargs = {key: kwargs[key] for key in kwargs if key in params }
            return cls.get_jsons(
                order_by=order_by, 
                page_num=page_num, 
                page_size=page_size,
                **kwargs
            )

    @classmethod
    def post(cls, data: dict):
        cls.add(data)

    @classmethod
    def put(cls, id: int, data: dict):
        cls.save(id, data)

    @classmethod
    def delete(cls, id: int):
        cls.delete_list(id=id)
