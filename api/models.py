from django.db import models
import datetime
# Create your models here.
class Vendor(models.Model):
    """
    This model stores essential information about each vendor and their performance metrics.
    """

    name = models.CharField(blank=True, max_length=100) #- Vendor's name.
    contact_details = models.TextField(blank=True) #- Contact information of the vendor.
    address = models.TextField(blank=True) #- Physical address of the vendor.
    vendor_code = models.CharField(blank=True, max_length=200) #- A unique identifier for the vendor.
    on_time_delivery_rate = models.FloatField(blank=True, default=0.0) #- Tracks the percentage of on-time deliveries.
    quality_rating_avg = models.FloatField(default=0.0, blank=True) #- Average rating of quality based on purchase orders.
    average_response_time = models.FloatField(default=0.0, blank=True)# - Average time taken to acknowledge purchase orders.
    fulfillment_rate = models.FloatField(default=0.0, blank=True) #- Percentage of purchase orders fulfilled successfully.

class PurchaseOrder(models.Model):
    """
    This model captures the details of each purchase order and is used to calculate various
    performance metrics.
    """
    OP = 'Order Placed'
    OC = 'Order Confirmed'
    SH = 'Shipped'
    DP = 'Dispatched'
    OD = 'Out for delivery'
    DD = 'Delivered'

    STATUS_CHOICES = (
        ('OP' , 'Order Placed'),
        ('OC' , 'Order Confirmed'),
        ('SH' , 'Shipped'),
        ('DP' , 'Dispatched'),
        ('OD' , 'Out for delivery'),
        ('DD' , 'Delivered'),
    )

    po_number = models.CharField(blank=True, max_length=150) # - Unique number identifying the PO.
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # - Link to the Vendor model.
    order_date = models.DateTimeField(default=datetime.datetime.now()) # - Date when the order was placed.
    delivery_date = models.DateTimeField(blank=True) # - Expected or actual delivery date of the order.
    items = models.JSONField(blank=True) # - Details of items ordered.
    quantity = models.IntegerField(blank=True) # - Total quantity of items in the PO.
    status = models.CharField(blank=True, choices=STATUS_CHOICES, default='OP', max_length=100) # - Current status of the PO (e.g., pending, completed, canceled).
    quality_rating = models.FloatField(null=True) # - Rating given to the vendor for this PO (nullable).
    issue_date = models.DateTimeField(blank=True) # - Timestamp when the PO was issued to the vendor.
    acknowledgment_date = models.DateTimeField(null=True) #, nullable - Timestamp when the vendor acknowledged the PO.
    delivered_date = models.DateField(null=True, blank=True) #Date to record when the delivery is made.

class HistoricalPerformance(models.Model):
    """
    This model optionally stores historical data on vendor performance, enabling trend analysis.
    """

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) #- Link to the Vendor model.
    date = models.DateTimeField(blank=True, default=datetime.datetime.now()) #- Date of the performance record.
    on_time_delivery_rate = models.FloatField(default=0.0, blank=True) #- Historical record of the on-time delivery rate.
    quality_rating_avg = models.FloatField(default=0.0, blank=True) #- Historical record of the quality rating average.
    average_response_time = models.FloatField(default=0.0, blank=True) #- Historical record of the average response time.
    fulfillment_rate = models.FloatField(default=0.0, blank=True) #- Historical record of the fulfilment rate.