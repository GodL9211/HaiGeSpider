class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data


class EventPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, event):
        for subscriber in self._subscribers:
            subscriber.update(event)


class EventSubscriber:
    def update(self, event):
        raise NotImplementedError("Subclasses should implement this!")


class ProductAddedEvent(Event):
    pass  # 可以添加更多与产品添加相关的属性


class InventoryLowEvent(Event):
    pass  # 可以添加更多与库存不足相关的属性


class DiscountSystem(EventSubscriber):
    def update(self, event):
        if isinstance(event, ProductAddedEvent):
            print(f"Applying discount rules for added product ID {event.data['product_id']}.")


class NotificationSystem(EventSubscriber):
    def update(self, event):
        if isinstance(event, InventoryLowEvent):
            print(f"Sending low inventory notification for product ID {event.data['product_id']}.")


class InventoryManagementSystem(EventSubscriber):
    def update(self, event):
        if isinstance(event, InventoryLowEvent):
            print(f"Triggering restocking process for product ID {event.data['product_id']}.")


def main():
    # 创建事件发布者
    event_publisher = EventPublisher()

    # 创建订阅者并注册到发布者
    discount_system = DiscountSystem()
    notification_system = NotificationSystem()
    inventory_management_system = InventoryManagementSystem()

    event_publisher.subscribe(discount_system)
    event_publisher.subscribe(notification_system)
    event_publisher.subscribe(inventory_management_system)

    # 模拟事件
    product_added_event = ProductAddedEvent(type="PRODUCT_ADDED", data={"product_id": 123})
    inventory_low_event = InventoryLowEvent(type="INVENTORY_LOW", data={"product_id": 456})

    # 发布事件
    event_publisher.notify(product_added_event)  # 优惠系统将响应
    event_publisher.notify(inventory_low_event)  # 通知系统和库存管理系统将响应


if __name__ == "__main__":
    main()

# Applying discount rules for added product ID 123.
# Sending low inventory notification for product ID 456.
# Triggering restocking process for product ID 456.
