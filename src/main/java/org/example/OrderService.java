package org.example;

public class OrderService {
    private final PaymentService paymentService;
    private final InventoryService inventoryService;
    private final NotificationService notificationService;

    public OrderService(PaymentService paymentService, InventoryService inventoryService, NotificationService notificationService) {
        this.paymentService = paymentService;
        this.inventoryService = inventoryService;
        this.notificationService = notificationService;
    }

    public void placeOrder(Order order) {
        if (!inventoryService.isProductAvailable(order.getProduct(), order.getQuantity())) {
            throw new IllegalStateException("Product not available");
        }

        if (!paymentService.processPayment(order)) {
            throw new IllegalStateException("Payment failed");
        }

        notificationService.sendOrderConfirmation(order);
    }
}
