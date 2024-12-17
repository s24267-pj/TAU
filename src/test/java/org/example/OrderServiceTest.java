package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class OrderServiceTest {

    private OrderService orderService;
    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;

    @BeforeEach
    void setUp() {
        paymentService = mock(PaymentService.class);
        inventoryService = mock(InventoryService.class);
        notificationService = mock(NotificationService.class);
        orderService = new OrderService(paymentService, inventoryService, notificationService);
    }

    @Test
    void shouldPlaceOrderSuccessfully() {
        Order order = new Order("product1", 1);

        when(inventoryService.isProductAvailable("product1", 1)).thenReturn(true);
        when(paymentService.processPayment(order)).thenReturn(true);

        assertDoesNotThrow(() -> orderService.placeOrder(order));

        verify(inventoryService).isProductAvailable("product1", 1);
        verify(paymentService).processPayment(order);
        verify(notificationService).sendOrderConfirmation(order);
    }

    @Test
    void shouldFailWhenProductNotAvailable() {
        Order order = new Order("product1", 1);

        when(inventoryService.isProductAvailable("product1", 1)).thenReturn(false);

        Exception exception = assertThrows(IllegalStateException.class, () -> orderService.placeOrder(order));

        assertEquals("Product not available", exception.getMessage());
        verify(inventoryService).isProductAvailable("product1", 1);
        verifyNoInteractions(paymentService, notificationService);
    }

    @Test
    void shouldFailWhenPaymentNotProcessed() {
        Order order = new Order("product1", 1);

        when(inventoryService.isProductAvailable("product1", 1)).thenReturn(true);
        when(paymentService.processPayment(order)).thenReturn(false);

        Exception exception = assertThrows(IllegalStateException.class, () -> orderService.placeOrder(order));

        assertEquals("Payment failed", exception.getMessage());
        verify(inventoryService).isProductAvailable("product1", 1);
        verify(paymentService).processPayment(order);
        verifyNoInteractions(notificationService);
    }

    @Test
    void shouldHandlePaymentServiceException() {
        Order order = new Order("product1", 1);

        when(inventoryService.isProductAvailable("product1", 1)).thenReturn(true);
        when(paymentService.processPayment(order)).thenThrow(new RuntimeException("Payment service error"));

        Exception exception = assertThrows(RuntimeException.class, () -> orderService.placeOrder(order));

        assertEquals("Payment service error", exception.getMessage());
        verify(inventoryService).isProductAvailable("product1", 1);
        verify(paymentService).processPayment(order);
        verifyNoInteractions(notificationService);
    }
}
